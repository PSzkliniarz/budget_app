<template>
  <div class="container text-dark">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">Please sign in</h1>

        <p v-if="incorrectAuth">Incorrect username or password entered - please try again</p>
        <form v-on:submit.prevent="login">
          <div class="form-group">
            <input type="text" name="username" id="user" v-model="username" class="form-control" placeholder="Username">
          </div>
          <div class="form-group">
            <input type="password" name="password" id="pass" v-model="password" class="form-control" placeholder="Password">
          </div>
          <button type="submit" class="btn btn-lg btn-primary btn-block">Login</button>
          <button @click="$router.push('/registration')" class="btn btn-lg btn-primary btn-block">Rejestracja</button>
        </form>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data () {
    return {
      username: '',
      password: '',
      incorrectAuth: false
    }
  },
  methods: {
    login () {
      this.$store.dispatch('userLogin', {
        username: this.username,
        password: this.password
      })
          .then( () => {
            this.$router.push({name: 'home'})
          })
          .catch(err => {
            console.log(err)
            this.incorrectAuth = true
          })

    }
  }
}
</script>

<style scoped>

</style>