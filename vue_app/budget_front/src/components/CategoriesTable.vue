<template>
  <div>
    <v-card>
      <div class="table-header">
        <h1>Kategorie</h1>
        <button class="blue-button" @click="addCategoryDialog = !addCategoryDialog">dodaj kategorie</button>
      </div>
      <v-data-table
          :headers="headers"
          :items="getCategories || []"
          :items-per-page="5"
          class="elevation-1"
          :search="search"
      >
        <template v-slot:top>
          <v-text-field
              v-model="search"
              label="Szukaj kategori"
              class="mx-4"
          ></v-text-field>
        </template>
        <template v-slot:[`item.title`]="{ item }">
          {{ capitalize(item.name) }}
        </template>
      </v-data-table>
    </v-card>
    <v-dialog v-model="addCategoryDialog" max-width="600">
      <add-category v-if="addCategoryDialog" @close-dialog="addCategoryDialog=false"/>
    </v-dialog>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import AddCategory from "@/components/forms/AddCategory";

export default {
  name: "CategoriesTable",
  components: {AddCategory},
  data() {
    return {
      search: '',
      addCategoryDialog: false
    }
  },
  computed: {
    ...mapGetters(['getCategories']),
    headers() {
      return [
        {text: 'Nazwa', value: 'name'},
      ]
    },
  },
  methods: {
    ...mapActions(['loadCategories']),
    capitalize(str) {
      return str[0].toUpperCase() + str.slice(1);
    }
  },
  created() {
    this.loadCategories();
  },
}
</script>

<style scoped>
.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>