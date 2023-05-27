<template>

  <v-row class="text-center">
    <v-col cols="12">
      <h1>Accounts test</h1>
      {{ getExpenses }}
      <h2>Categories</h2>
      {{ getCategories }}
    </v-col>

  </v-row>

</template>

<script>
import { mapActions, mapGetters} from "vuex";

export default {
  name: 'AccountsTest',
  computed: {
    ...mapGetters(['getExpenses', 'getCategories'])
  },
  methods: {
     ...mapActions(['loadExpenses', 'loadCategories'])
  },
  created() {
    this.loadExpenses();
    this.loadCategories();
  },
}
</script>
