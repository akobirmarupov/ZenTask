from rest_framework import serializers
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'), username=email, password=password
            )

            if not user:
                raise serializers.ValidationError('Email yoki parol xato.')
            
            if not user.is_active:
                raise serializers.ValidationError('Ushbu hisob faol emas.')
            
            # if not user.is_confirmed:
            #     raise serializers.ValidationError('Ushbu hisob hali mavjuda emas yoki hali tasdiqlanmagan.')
            
        else:
            raise serializers.ValidationError('Email va parolni kiritish shart!')
        
        data['user'] = user
        return data
    


class RegisterInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()