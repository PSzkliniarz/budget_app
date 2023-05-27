<template>
  <v-app>
   <v-app-bar app>
      <v-app-bar-nav-icon @click="toggleDrawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Moja aplikacja</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer
        v-if="drawerOpen"
      v-model="drawerOpen"
      absolute
      bottom
      temporary
      :style="drawerStyle"
    >
      <v-list>
        <v-list-item v-for="(item, index) in menuItems" :key="index" @click="selectMenuItem(item)">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <v-container>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data() {
    return {
      drawerOpen: false,
      miniVariant: false,
      isMobile: false,
      menuItems: [
        { title: 'Strona główna', icon: 'mdi-home' },
        { title: 'O nas', icon: 'mdi-information' },
        { title: 'Kontakt', icon: 'mdi-email' }
      ]
    };
  },
  mounted() {
    this.checkMobile();
    window.addEventListener('resize', this.checkMobile);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkMobile);
  },
  computed: {
    drawerStyle() {
      if (this.isMobile) {
        // Zwracaj style inline w zależności od szerokości ekranu
        return {
          height: '200px',
          backgroundColor: 'lightblue'
        };
      } else {
        return {}; // Puste style, gdy szerokość ekranu jest większa
      }
    }
  },
  methods: {
    toggleDrawer() {
      this.drawerOpen = !this.drawerOpen;
    },
    selectMenuItem(item) {
      switch (item.title) {
        case 'Strona główna':
          this.$router.push('/');
          break;
        case 'O nas':
          this.$router.push('/about');
          break;
        case 'Kontakt':
          this.$router.push('/logout');
          break;
        default:
          break;
      }
    },
    checkMobile() {
      this.isMobile = window.innerWidth <= 1265; // Dostosuj szerokość do swojego poziomu responsywności
      this.miniVariant = this.isMobile;
    }
  }
};
</script>
<style>

</style>
