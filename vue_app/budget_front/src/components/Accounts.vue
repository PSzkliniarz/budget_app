<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <h1>Accounts test</h1>
        {{ APIData }}
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
import {getAPI} from "@/axios-api";

  export default {
    name: 'AccountsTest',

    data: () => ({
      APIData: []
    }),
    created() {
      getAPI.get('/accounts/',)
          .then(response => {
            console.log('API work')
            this.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          })
    }
  }
</script>
