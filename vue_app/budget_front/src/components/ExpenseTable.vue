<template>
  <v-card>
    <div class="table-header">
      <h1>Wydatki</h1>
      <button @click="addExpenseDialog = true">dodaj wydatek</button>
    </div>
    <v-data-table
        :headers="headers"
        :items="getActualExpenses || []"
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
  </v-card>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "ExpenseTable",
  data() {
    return {
      search: '',
      addExpenseDialog: false,
    }
  },
  computed: {
    ...mapGetters(['getActualExpenses']),
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

.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

button {
  margin: 20px;
  margin-top: 0;
  padding: 1% 3%;
  border-radius: 10px;
  background-color: #4094E1;
  color: #FFFFFF;
  font-width: bold;
}
</style>