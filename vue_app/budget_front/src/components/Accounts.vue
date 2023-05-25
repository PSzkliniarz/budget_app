<template>

  <v-row class="text-center">
    <v-col cols="12">
      <h1>Accounts test</h1>
      {{ APIData }}
      <h2>Categories</h2>
      {{ category }}
    </v-col>

  </v-row>

</template>

<script>
import axiosInstance from "@/axios-api";
import {mapState} from "vuex";

export default {
  name: 'AccountsTest',
  computed: mapState(['APIData', 'category']),
  created() {
    axiosInstance.get('/expense/')
        .then(response => {
          this.$store.state.APIData = response.data
        })
        .catch(err => {
          console.log(err)
        })
    axiosInstance.get('/category/')
  .then(response => {
    this.$store.state.category = response.data;
  })
  .catch(err => {
    console.log(err);
  });
  }
}
</script>
