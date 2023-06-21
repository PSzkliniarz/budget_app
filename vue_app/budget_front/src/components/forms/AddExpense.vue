<template>

  <v-card class="form-card">
  <h1>Dodaj wydatek</h1>
    <v-text-field
        v-model="newExpense.title"
        label="Nazwa wydatku"
        :rules="rules"
    />
    <v-text-field
        v-model.number="newExpense.amount"
        label="Wartość"
        type="number"
        :rules="rules"
    />
    <v-date-picker v-model="newExpense.data" elevation="1" :rules="rules"/>
    <v-select
        v-model.number="newExpense.category"
        :items="getCategories || []"
        item-text="name"
        item-value="id"
        label="Kategoria"
        :rules="rules"
    />
    <div class="card-actions">
      <button class="blue-button" @click="addExpense" :disabled="!validForm">dodaj</button>
      <button class="blue-button" @click="$emit('close-dialog')">anuluj</button>
    </div>
  </v-card>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import axiosInstance from "@/axios-api";

export default {
  name: "AddExpense",
  data() {
    return {
      newExpense: {
        title: '',
        amount: null,
        data: null,
        category: null
      },
      rules: [
          value => !!value || 'Pole wymagane.',
      ]
    }
  },
  computed: {
    ...mapGetters(['getCategories']),
    validForm() {
      return (
        this.newExpense.title !== ""
          && this.newExpense.amount !== null && this.newExpense.amount !== ""
          && this.newExpense.data !== null && this.newExpense.data !== ""
          && this.newExpense.category !== null && this.newExpense.category !== ""
      );
    },
  },
  methods: {
    ...mapActions(['loadCategories', 'loadExpenses']),
    addExpense() {
      axiosInstance.post('/expense/', this.newExpense )
        .then(() => {
          this.loadExpenses()
          this.$emit('close-dialog')
        })
        .catch(err => {
          console.log(err)
        })

      this.$emit('close-dialog')
    }
  },
  created() {
    this.loadCategories();
  },
}
</script>
<style scoped>
.form-card {
  margin-top: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.card-actions {
  margint-top: 20px;
  display: flex;
  justify-content: space-between;
}

</style>