<template>

  <v-card class="form-card">
    <h1>{{ header }}</h1>
    <h3 class="mt-4">{{ text }}</h3>
    <v-text-field
        v-if="header==='Zmień nazwę kategorii'"
        v-model="newCategoryName"
        label="Nowa nazwa kategori"
        :rules="rules"
    />
    <div v-if="text !== 'Przed usunięciem usuń wszystkie wydatki dla tej kategori'" class="card-actions mt-4">
      <button
          v-if="header!=='Zmień nazwę kategorii'"
          class="blue-button"
          @click="$emit('delete-item')"
      >
        usuń
      </button>
      <button v-else class="blue-button" @click="editCategory">zmień</button>
      <button class="blue-button" @click="$emit('close-delete-dialog')">anuluj</button>
    </div>
    <div v-else class="card-actions mt-4 justify-center">
      <button class="blue-button" @click="$emit('close-delete-dialog')">ok</button>
    </div>
  </v-card>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "DeleteDialog",
  props: ['header', 'text',],
  data() {
    return {
      newCategoryName: '',
      categoriesNames: [],
      rules: [
          value => !!value || 'Wprowadź nazwę.',
          value => !this.categoriesNames.includes(value)  || 'Kategoria już istnieje'
      ]
    }
  },
  computed: {
    ...mapGetters(['getCategories']),
  },
  methods: {
    editCategory() {
      this.$emit('edit-item', this.newCategoryName)
    }
  },
  mounted() {
    this.categoriesNames = this.getCategories.map(cat => cat.name)
  }
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