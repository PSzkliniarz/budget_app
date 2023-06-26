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
          class="elevation-1 mt-5"
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
        <template v-slot:[`item.edit`]="{item}">
          <v-icon
              @click="selectToEdit(item)"
          >
            mdi-pencil
          </v-icon>
          <v-icon
              @click="selectToDelete(item)"
          >
            mdi-delete
          </v-icon>
        </template>
      </v-data-table>
    </v-card>
    <v-dialog v-model="addCategoryDialog" max-width="600">
      <add-category v-if="addCategoryDialog" @close-dialog="addCategoryDialog=false"/>
    </v-dialog>
    <v-dialog v-model="editCategoryDialog" max-width="600">
      <delete-dialog
          v-if="editCategoryDialog"
          @close-dialog="editCategoryDialog=false"
          :header="editDialogHeader"
          :text="editDialogText"
          @edit-item="editCategory"
          @close-delete-dialog="editCategoryDialog=false"
      />
    </v-dialog>
    <v-dialog v-model="deleteCategoryDialog" max-width="600">
      <delete-dialog
          v-if="deleteCategoryDialog"
          @close-dialog="deleteCategoryDialog=false"
          :header="deleteDialogHeader"
          :text="deleteDialogText"
          @delete-item="deleteCategory"
          @close-delete-dialog="deleteCategoryDialog=false"
      />
    </v-dialog>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import AddCategory from "@/components/forms/AddCategory";
import DeleteDialog from "@/components/forms/DeleteDialog";
import axiosInstance from "@/axios-api";

export default {
  name: "CategoriesTable",
  components: {AddCategory, DeleteDialog},
  data() {
    return {
      search: '',
      customRowsPerPageText: 'Liczba wierszy na stronę:',
      addCategoryDialog: false,
      editCategoryDialog: false,
      editDialogHeader: 'Zmień nazwę kategorii',
      editDialogText: '',
      deleteCategoryDialog: false,
      deleteDialogHeader: 'Usuń kategorie',
      deleteDialogText: '',
      selectedItem: null
    }
  },
  computed: {
    ...mapGetters(['getCategories', 'getExpenses']),
    headers() {
      return [
        {text: 'Nazwa', value: 'name'},
        {text: 'Edyuj/Usuń', value: 'edit', align: 'end'},
      ]
    },
  },
  methods: {
    ...mapActions(['loadCategories']),
    capitalize(str) {
      return str[0].toUpperCase() + str.slice(1);
    },
    selectToEdit(item) {
      this.selectedItem = item
      this.editeDialogText = `Czy na pewno chcesz zmienić nazwę kategorii ${item.name} ?`
      this.editCategoryDialog = true
    },
    selectToDelete(item) {
      if (this.getExpenses.some(exp => exp.category === item.id)) {
        this.deleteDialogText = 'Przed usunięciem usuń wszystkie wydatki dla tej kategori'
      } else {
        this.deleteDialogText = `Czy na pewno chcesz usunąc kategorie ${item.name} ?`
        this.selectedItem = item
      }
      this.deleteCategoryDialog = true
    },
    editCategory(newCategoryName) {
      this.editCategoryDialog = false
      axiosInstance.put(`/category/${this.selectedItem.id}/`, {
        id: this.selectedItem.id,
        name: newCategoryName
      })
          .then(() => {
            this.loadCategories()
          })
          .catch(err => {
            console.log(err)
          })
    },
    deleteCategory() {
      this.deleteCategoryDialog = false
      axiosInstance.delete(`/category/${this.selectedItem.id}/`)
          .then(() => {
            this.loadCategories()
          })
          .catch(err => {
            console.log(err)
          })
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

.blue-button {
  padding: 0.5% 2%;
}

</style>