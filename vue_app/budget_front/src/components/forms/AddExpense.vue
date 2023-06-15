<template>

  <v-card>
  <h1>Add expense</h1>
    <button @click="addExpense">dodaj</button>
    <button @click="$emit('close-dialog')">anuluj</button>
  </v-card>
</template>

<script>
export default {
  name: "AddExpense",
  methods: {
    addExpense() {
      this.$emit('close-dialog')
    }
  }
}
</script>