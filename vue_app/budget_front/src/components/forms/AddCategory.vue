<template>

  <v-card class="form-card">
    <h1>Dodaj kategorie</h1>
    <v-text-field
        v-model="newCategoryName"
        label="Nazwa kategori"
        :rules="rules"
    />
    <div class="card-actions">
      <button class="blue-button" @click="addCategory" :disabled="!validForm">dodaj</button>
      <button class="blue-button" @click="$emit('close-dialog')">anuluj</button>
    </div>
  </v-card>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import axiosInstance from "@/axios-api";

export default {
  name: "AddCategory",
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
    validForm() {
      return (
        this.newCategoryName !== "" &&
        !this.categoriesNames.includes(this.newCategoryName)
      );
    },
  },
  methods: {
    ...mapActions(['loadCategories']),
    addCategory() {
      axiosInstance.post('/category/', {name: this.newCategoryName} )
        .then(() => {
          this.loadCategories()
          this.$emit('close-dialog')
        })
        .catch(err => {
          console.log(err)
        })

      this.$emit('close-dialog')
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