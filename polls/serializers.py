from rest_framework import serializers
from polls.models import Citizen

class CitizenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Citizen
		fields = '__all__'

