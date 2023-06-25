<template>
  <div>
    <v-card>
      <div class="table-header">
        <h1>Wydatki</h1>
        <button class="blue-button" @click="addExpenseDialog = !addExpenseDialog">dodaj wydatek</button>
      </div>
      <v-data-table
          :headers="headers"
          :items="getActualExpenses || []"
          :items-per-page="5"
          class="elevation-1 mt-5"
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
        <template v-slot:[`item.delete`] ="{item}">
          <v-icon
            @click="selectToDelete(item)"
            >
            mdi-delete
          </v-icon>
        </template>
      </v-data-table>
    </v-card>
    <v-dialog v-model="addExpenseDialog" max-width="600">
      <add-expense v-if="addExpenseDialog" @close-dialog="addExpenseDialog=false"/>
    </v-dialog>
    <v-dialog v-model="deleteExpenseDialog" max-width="600">
      <delete-dialog
          v-if="deleteExpenseDialog"
          @close-dialog="deleteExpenseDialog=false"
          :header="deleteDialogHeader"
          :text="deleteDialogText"
          @delete-item="deleteExpense"
          @close-delete-dialog="deleteExpenseDialog=false"
      />
    </v-dialog>
  </div>

</template>

<script>
import {mapActions, mapGetters} from "vuex";
import AddExpense from "@/components/forms/AddExpense";
import DeleteDialog from "@/components/forms/DeleteDialog";
import axiosInstance from "@/axios-api";

export default {
  name: "ExpenseTable",
  components: {AddExpense, DeleteDialog},
  data() {
    return {
      search: '',
      addExpenseDialog: false,
      deleteExpenseDialog: false,
      deleteDialogHeader: 'Usuń wydatek',
      deleteDialogText: '',
      itemToDelete: null
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
        {text: 'Usuń', value: 'delete', align: 'end'},
      ]
    },
  },
  methods: {
    ...mapActions(['loadExpenses']),
    capitalize(str) {
      return str[0].toUpperCase() + str.slice(1);
    },
    selectToDelete(item) {
      this.itemToDelete = item
      this.deleteDialogText = `Czy na pewno chcesz usunąc ${item.title} z dnia ${item.data}?`
      this.deleteExpenseDialog = true
    },
    deleteExpense(){
      this.deleteExpenseDialog = false
      axiosInstance.delete(`/expense/${this.itemToDelete.id}/`)
          .then(() => {
            this.loadExpenses()
          })
          .catch(err => {
            console.log(err)
          })
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

.blue-button {
  padding: 0.5% 2%;
}

</style>