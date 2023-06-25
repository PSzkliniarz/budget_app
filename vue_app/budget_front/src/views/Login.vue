<template>
  <div class="v-card-container">
    <v-card width="600" class="mt-0">
      <h1>Login</h1>
      <v-text-field v-model="username" label="Login" :rules="usernameRules"/>
      <v-text-field v-model="password" label="Password" type="password" :rules="passwordRules"/>
      <div class="button-container">
        <p v-if="incorrectAuth" style="color: red; margin: -10px auto 10px auto">Nieprawidłowy login lub hasło</p>
        <button class="blue-button" @click="login" :disabled="!isFormValid">Zaloguj</button>
        <button @click="$router.push('/registration')" class="register-button">Nie masz konta? Zarejestruj się</button>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      username: '',
      password: '',
      incorrectAuth: false,

      usernameRules: [
        v => !!v || 'Login jest wymagany',
      ],
      passwordRules: [
        v => !!v || 'Hasło jest wymagane',
      ],
    }
  },
  computed: {
    isFormValid() {
      return this.username && this.password;
    }
  },
  methods: {
    login() {
      this.$store.dispatch('userLogin', {
        username: this.username,
        password: this.password
      }).then(() => {
        this.$router.push({name: 'home'})
      }).catch(err => {
        console.log(err)
        this.incorrectAuth = true
      })
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

.register-button {
  margin-top: 15px;
  color: #4094E1;
}
</style>