<template>
  <div class="v-card-container">
    <v-card width="600" class="mt-0">
      <h1>Rejestracja</h1>
      <v-text-field v-model="user.username" label="Login" :rules="usernameRules"/>
      <v-text-field v-model="user.password" label="Password" type="password" :rules="passwordRules"/>
      <v-text-field v-model="user.email" label="Email" :rules="emailRules"/>
      <div class="button-container">
        <button class="blue-button" @click="registerUser" :disabled="!isFormValid">Zarejestruj</button>
        <button @click="$router.push('/login')" class="login-button">Masz już konto? Zaloguj się</button>

      </div>
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
        v => (v && v.length >= 5) || 'Hasło musi mieć minimum 5 znaków',
        v => /[!@#$%^&*(),.?":{}|<>]/.test(v) || 'Hasło musi zawierać znak specjalny'
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
  height: 91vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

v-card {
  height: fit-content;
}

.button-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 16px;
}

.login-button {
  margin-top: 15px;
  color: #4094E1;
}
</style>
