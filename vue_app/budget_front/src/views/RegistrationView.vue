<template>
  <div class="v-card-container">
    <v-card max-width="600">
      <v-text-field v-model="user.username" label="Login" :rules="usernameRules"/>
      <v-text-field v-model="user.password" label="Password" type="password" :rules="passwordRules"/>
      <v-text-field v-model="user.email" label="Email" :rules="emailRules"/>
      <v-btn @click="registerUser" :disabled="!isFormValid">Zarejestruj</v-btn>
    </v-card>
  </div>
</template>

<script>
import axiosInstance from "@/axios-api";

export default {
  name: "RegistrationView",
  data() {
    return {
      user: {
        username: '',
        password: '',
        email: ''
      },
      usernameRules: [
        v => !!v || 'Login jest wymagany',
      ],
      passwordRules: [
        v => !!v || 'Hasło jest wymagane',
      ],
      emailRules: [
        v => !!v || 'Email jest wymagany',
        v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'Nieprawidłowy format email'
      ]
    }
  },
  computed: {
    isFormValid() {
      return this.user.username && this.user.password && this.user.email;
    }
  },
  methods: {
    registerUser() {
      axiosInstance.post('/user-create/', this.user)
        .then(() => {
          this.$router.push('/login');
        })
        .catch(error => {
          console.log(error.response);
        });
    }
  }
}
</script>

<style scoped>
.v-card-container {
  display: flex;
  justify-content: center;
  align-content: center;
}
</style>
