<template>

  <v-card class="form-card">
    <h1>{{header}}</h1>
    <h3 class="mt-4">{{text}}</h3>
    <div class="card-actions mt-4">
      <button class="blue-button" @click="$emit('delete-item')">usuń</button>
      <button class="blue-button" @click="$emit('close-delete-dialog')">anuluj</button>
    </div>
  </v-card>
</template>

<script>
export default {
  name: "DeleteDialog",
  props: ['header', 'text',]
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
  display: flex;
  justify-content: space-between;
}
</style>