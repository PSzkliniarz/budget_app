<template>
  <div>
    <h1>Wydatki</h1>
    <v-data-table
        :headers="headers"
        :items="getExpenses || []"
        :items-per-page="5"
        class="elevation-1"
        :search="search"
    >
      <template v-slot:top>
        <v-text-field
            v-model="search"
            label="Szukaj wydatku"
            class="mx-4"
        ></v-text-field>
      </template>
      <template v-slot:[`item.title`]="{ item }">
        {{ capitalize(item.title) }}
      </template>
    </v-data-table>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "ExpenseTable",
  data() {
    return {
      search: '',
    }
  },
  computed: {
    ...mapGetters(['getExpenses']),
    headers() {
      return [
        {text: 'Nazwa', value: 'title'},
        {text: 'Wartość', value: 'amount'},
        {text: 'Data', value: 'data'},
        {text: 'Kategoria', value: 'category_name'},
      ]
    },
  },
  methods: {
    ...mapActions(['loadExpenses']),
    capitalize(str) {
      return str[0].toUpperCase() + str.slice(1);
    }
  },
  created() {
    this.loadExpenses();
  },
}
</script>

<style scoped>

</style>