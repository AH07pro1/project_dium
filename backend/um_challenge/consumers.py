from channels.generic.websocket import AsyncWebsocketConsumer
import json
import random
from um_challenge.models import Um_Compete
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async


class ChallengeConsumer(AsyncWebsocketConsumer):

    participants = []

    def __init__(self) -> None:
        super().__init__()
        self.tag = ""

    @database_sync_to_async
    def save_game(self, game):
        game.save()

    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['challenge_id']

        self.room_group_name = 'room_%s' % self.room_name

        # Add the client to a group and send the current state to the client
        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Remove the client from the group
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)

        self.participants.remove(self.tag)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')

        self.game = await sync_to_async(
            Um_Compete.objects.get)(um_compete_challenge_id=self.room_name)

        if action == "start":
            #generate teams
            start = text_data_json.get("start")

            #sampledMembers = self.game.accepted_members.copy()
            #random.shuffle(sampledMembers)
            #print(sampledMembers)
            #if len(sampledMembers) % 2 == 0:  # Even case
            #team1 = sampledMembers[:len(sampledMembers) // 2]
            #team2 = sampledMembers[len(sampledMembers) // 2:]
            # else:  # Odd case
            #team1 = sampledMembers[:len(sampledMembers) // 2 + 1]
            #team2 = sampledMembers[len(sampledMembers) // 2 + 1:]

            #self.game.team_1 = team1
            #self.game.team_2 = team2

            #await self.save_game(self.game)
            await self.channel_layer.group_send(self.room_group_name, {
                "type": "start_update",
                "start": True,
            })

            #await self.channel_layer.group_send(self.room_group_name, {
            #"type": "start_teams",
            #"team1": team1,
            #"team2": team2,
            #})

        if action == "join":
            # Update the model and broadcast the update to the group
            user_tag = text_data_json.get('user_tag')
            self.tag = user_tag
            print(self.participants)
            if user_tag not in self.participants:
                self.participants.append(user_tag)

            self.channel_layer.group_send(self.room_group_name, {
                'type': 'update_participants',
                'participants': self.participants
            })

            await self.channel_layer.group_send(
                self.room_group_name, {
                    "type": "send_participants",
                    "participants": self.participants,
                })

            await self.channel_layer.group_send(self.room_group_name, {
                "type": "user_join",
                "user_tag": user_tag,
            })

        if action == "finish":
            # Update the model and broadcast the update to the group
            finished = text_data_json.get('finished')
            self.participants = []
            await self.channel_layer.group_send(self.room_group_name, {
                "type": "finish_update",
                "finished": finished,
            })

        if action == "score":
            score = text_data_json.get('score')
            team = text_data_json.get('team')

            if team == "1":
                self.game.team_1_score.append(score)
                await self.save_game(self.game)

                await self.channel_layer.group_send(self.room_group_name, {
                    "type": "score_update",
                    "score": score,
                    "team": team
                })
            if team == "2":
                self.game.team_2_score.append(score)
                await self.save_game(self.game)
                await self.channel_layer.group_send(self.room_group_name, {
                    "type": "score_update",
                    "score": score,
                    "team": team
                })

        if action == "team":
            team1 = text_data_json["team1"]
            team2 = text_data_json["team2"]
            print(f" team 1 is:{team1}")
            print(f" team 2 is:{team2}")

            await self.channel_layer.group_send(self.room_group_name, {
                "type": "team_update",
                "team1": team1,
                "team2": team2
            })

        if action == "stopquestion":
            stop = text_data_json('stop')
            await self.channel_layer.group_send(self.room_group_name, {
                "type": "stop_question",
                "stopnumber": stop
            })

        if action == "userscore":
            score = text_data_json.get('score')
            team = text_data_json.get('team')

            await self.channel_layer.group_send(self.room_group_name, {
                "type": "userscore_update",
                "score": score,
                "team": team
            })

        if action == "next":
            index = text_data_json['index']
            print(f"index is {index}")
            await self.channel_layer.group_send(self.room_group_name, {
                "type": "next_question",
                "index": index
            })

        if action == "userfinishquestion":
            usertag = text_data_json['tag']
            correct = text_data_json["correct"]
            team = text_data_json['team']

            print(f"{usertag} correct = {correct} and is from team : {team}")
            await self.channel_layer.group_send(
                self.room_group_name, {
                    "type": "user_finish_question",
                    "usertag": usertag,
                    "correct": correct,
                    'team': team
                })

        if action == "quizdone":
            grade = text_data_json['grade']
            team = text_data_json['team']
            print(f"user is from team {team} and has {grade}")
            await self.channel_layer.group_send(self.room_group_name, {
                "type": "quiz_done",
                "grade": grade,
                "team": team
            })

        if action == "hostuserjoin":
            participants = text_data_json['participants']
            self.participants = participants

            await self.channel_layer.group_send(self.room_group_name, {
                "type": "send_participants",
                "participants": participants
            })

        if action == "questionstart":
            questionstart = text_data_json['questionstart']

            await self.channel_layer.group_send(self.room_group_name, {
                "type": "question_start",
                "questionstart": questionstart
            })

    async def question_start(self, event):
        questionstart = event.get('questionstart')
        await self.send(text_data=json.dumps({
            "type": "startquestion",
            "questionstart": questionstart,
        }))

    async def user_join(self, event):
        # Send the update to the client
        user_tag = event.get('user_tag')
        await self.send(text_data=json.dumps({
            "type": "join",
            "user_tag": user_tag,
        }))

    def update_participants(self, event):
        participants = event['participants']
        self.send(text_data=json.dumps({'participants': participants}))

    async def send_participants(self, event):

        await self.send(text_data=json.dumps({
            "type": "participation",
            "participants": self.participants
        }))

    async def userscore_update(self, event):
        score = event.get('score')
        team = event.get("team")

        await self.send(text_data=json.dumps({
            "type": "userscore",
            "score": score,
            "team": team
        }))

    async def quiz_done(self, event):
        #send this to host of challenge
        grade = event.get('grade')
        team = event.get('team')
        await self.send(text_data=json.dumps({
            "type": "quizdone",
            "grade": grade,
            "team": team
        }))

    async def user_finish_question(self, event):
        usertag = event.get('usertag')
        correct = event.get('correct')
        team = event.get('team')
        await self.send(text_data=json.dumps({
            "type": "userfinish",
            "usertag": usertag,
            'correct': correct,
            'team': team
        }))

    async def finish_update(self, event):
        # Send the update to the client
        finished = event.get('finished')
        await self.send(text_data=json.dumps({
            "type": "finish",
            "finished": finished,
        }))

    async def team_update(self, event):
        team1 = event.get('team1')
        team2 = event.get('team2')

        await self.send(text_data=json.dumps({
            "type": "team",
            "team1": team1,
            'team2': team2
        }))

    async def stop_question(self, event):
        stop = event.get("stop")
        await self.send(text_data=json.dumps({"type": "team", "stop": stop}))

    async def start_update(self, event):
        start = event.get('start')
        # Send the update to the client
        await self.send(text_data=json.dumps({
            "type": "start",
            "start": start,
        }))

    async def next_question(self, event):
        index = event.get('index')
        await self.send(text_data=json.dumps({"type": "next", "index": index}))

    #await self.send(self.room_group_name, {
    #"team1": team1,
    #"team2": team2,
    #})
    async def score_update(self, event):
        score = event.get('score')
        team = event.get('team')
        await self.send(text_data=json.dumps({
            "type": "score_update",
            "score": score,
            "team": team
        }))

    async def send_current_state(self):
        # Retrieve the current state of the model and send it to the client
        # You will need to implement this method based on your Django model structure
        pass

    async def update_model_add_user(self, user_tag):
        # Update the "accepted_members" field of the model to add the user's tag
        # You will need to implement this method based on your Django model structure
        pass

    async def update_model_set_finished(self, finished):
        # Update the "finished" field of the model to the specified value
        # You will need to implement this method based on your Django model structure

        pass