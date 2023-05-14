<template>

</template>

<script>
import {mapState} from "vuex";

export default {
  name: "TestView",
  computed: mapState(['APIData']),
  created() {
    getAPI.get('/accounts/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          this.$store.state.APIData = response.data
        })
        .catch(err => {
          console.log(err)
        })
  }
}
</script>

<style scoped>

</style>