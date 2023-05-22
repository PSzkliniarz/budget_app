<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <h1>Accounts test</h1>
        {{ APIData }}
        <h2>Categories</h2>
        {{category}}
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
import {getAPI} from "@/axios-api";
import {mapState} from "vuex";

  export default {
    name: 'AccountsTest',
    computed: mapState(['APIData', 'category']),
    created() {
      getAPI.get('/expense/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(response => {
            this.$store.state.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          })
      getAPI.get('/category/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
          .then(response => {
            this.$store.state.category = response.data
          })
          .catch(err => {
            console.log(err)
          })
    }
  }
</script>
