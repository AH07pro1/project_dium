from rest_framework import generics
from .models import SentShrtTrmCh, ReceivedShrtTrmCh
from .serializer import SendShrtTrmSerializer, ReceivedShrtTrmSerializer


# Sent Challenges branch
class AllSentChallenges(generics.ListAPIView):
    queryset = SentShrtTrmCh.objects.all()
    serializer_class = SendShrtTrmSerializer

all_sent_challenges = AllSentChallenges.as_view()

class CreateSentChallenges(generics.CreateAPIView):
    queryset = SentShrtTrmCh.objects.all()
    serializer_class = SendShrtTrmSerializer

create_sent_challenges = CreateSentChallenges.as_view()

class DetailSentChallenge(generics.RetrieveAPIView):
    queryset = SentShrtTrmCh.objects.all()
    serializer_class = SendShrtTrmSerializer
    lookup_field = "challenge_id"
    lookup_url_kwarg = "challenge_id"

detail_sent_challenge = DetailSentChallenge.as_view()

# Received Challenge Branch

class AllReceivedChallenges(generics.ListAPIView):
    queryset = ReceivedShrtTrmCh.objects.all()
    serializer_class = ReceivedShrtTrmSerializer

all_received_challenges = AllReceivedChallenges.as_view()

class CreateReceivedChallenges(generics.CreateAPIView):
    queryset = ReceivedShrtTrmCh.objects.all()
    serializer_class = ReceivedShrtTrmSerializer

create_received_challenges = CreateReceivedChallenges.as_view()

class DetailReceivedChallenge(generics.RetrieveAPIView):
    queryset = ReceivedShrtTrmCh.objects.all()
    serializer_class = ReceivedShrtTrmSerializer
    lookup_field = "challenge_id"
    lookup_url_kwarg = "challenge_id"

detail_received_challenge = DetailReceivedChallenge.as_view()

class UpdateSentShrtCh(generics.UpdateAPIView):
    queryset = SendShrtTrmSerializer
    serializer_class = SendShrtTrmSerializer
    lookup_field = "challenge_id"
    lookup_url_kwarg = "challenge_id"

update_sent_shrt_ch = UpdateSentShrtCh.as_view()