<template>
  <v-app>
    <v-app-bar app>
      <v-app-bar-nav-icon @click="toggleDrawer"
                          style="background-color: #FFFFFF; color: #4094E1; border: 3px solid #4094E1"/>
      <v-toolbar-title style="width: 100%; text-align: center; font-size: 2rem; ">
        Aplikacja <span style="color: #4094E1; font-weight: bold">Moje wydatki</span>
      </v-toolbar-title>
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
      scrollTop: 0,
      drawerOpen: false,
      miniVariant: false,
      isMobile: false,
      menuItems: [
        {title: 'Strona główna', icon: 'mdi-home'},
        {title: 'Twoje kategorie', icon: 'mdi-view-list'},
        {title: 'Wyloguj', icon: 'mdi-logout'}
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
        const windowHeight = window.innerHeight;
        return {
          height: '200px',
          top: `${this.scrollTop + windowHeight - 200}px`
        };
      } else {
        return {
          top: `${this.scrollTop}px`,
        };
      }
    }
  },
  watch: {
    drawerOpen(newVal) {
      if (newVal) {
        this.calculateScrollTop();
      }
    }
  },
  methods: {
    calculateScrollTop() {
      this.scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
    },
    toggleDrawer() {
      this.drawerOpen = !this.drawerOpen;
    },
    selectMenuItem(item) {
      switch (item.title) {
        case 'Strona główna':
          this.$router.push('/');
          break;
        case 'Twoje kategorie':
          this.$router.push('/categories');
          break;
        case 'Wyloguj':
          this.$router.push('/logout');
          break;
        default:
          break;
      }
    },
    checkMobile() {
      this.isMobile = window.innerWidth <= 1265;
      this.miniVariant = this.isMobile;
    }
  }
};
</script>
<style>
@font-face {
  font-family: 'Montserrat';
  src: url('../public/fonts/Montserrat-VariableFont_wght.ttf') format('truetype');
}

body {
  font-family: 'Montserrat', sans-serif;
}

.v-toolbar {
  padding: 10px !important;
  height: inherit !important;
  box-shadow: 5px 4px 39px rgba(0, 0, 0, 0.15) !important;
}

.v-main {
  background-color: #E3E3E3;
}

.v-card {
  background-color: #f1f1f1 !important;
  margin-top: 36px;
  padding: 24px;
  box-shadow: 5px 4px 39px rgba(0, 0, 0, 0.15) !important;
}

.blue-button {
  margin: 0 20px;
  padding: 1% 3%;
  border-radius: 10px;
  background-color: #4094E1;
  color: #FFFFFF;
  font-width: bold;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

</style>
