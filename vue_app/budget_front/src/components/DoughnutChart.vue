<template>
  <v-card class="chart-container">
    <div class="filter-container">
      <v-select v-model="selectedPeriod" :items="periodOptions" label="Wybierz okres" @change="filterExpenses "/>
    </div>
    <div class="doughnut-div">
      <Doughnut v-if="filteredExpenses.length > 0" :data="chartData" :options="chartOptions" class="doughnut-chart"/>
      <h2 v-if="filteredExpenses.length === 0">Brak wydatków w tym okresie</h2>
      <span class="period-sum">{{ periodSum }}</span>
    </div>
    <div class="chart-navigation">
      <button class="blue-button" @click="showPreviousPeriod">poprzedni okres</button>
      <div class="date-div">
        {{ prettyDate }}
      </div>

      <button class="blue-button" @click="showNextPeriod">następny okres</button>
    </div>
  </v-card>
</template>

<script>
import {Doughnut} from 'vue-chartjs';
import {Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale} from 'chart.js';
import {mapGetters, mapActions} from 'vuex';

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale);

export default {
  name: 'DoughnutChart',
  components: {Doughnut},

  computed: {
    ...mapGetters(['getExpenses']),

    chartData() {
      const categoryData = this.getCategoryData();
      return {
        labels: categoryData.labels,
        datasets: [
          {
            label: 'Suma:',
            backgroundColor: categoryData.colors,
            data: categoryData.amounts,
          },
        ],
      };
    },

    chartOptions() {
      return {
        responsive: true,
      };
    },
    periodOptions() {
      return ['Miesiąc', 'Tydzień'];
    },
    periodSum() {
      return this.filteredExpenses.reduce((acc, obj) => acc + obj.amount, 0)
    },
    prettyDate() {
      const date = this.startData;

      const day = String(date.getDate()).padStart(2, '0'); // Pobranie dnia miesiąca i dodanie wiodącego zera
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const year = date.getFullYear(); // Pobranie roku

      return `${day}/${month}/${year}`;
    }
  },
  data() {
    return {
      selectedPeriod: 'Miesiąc',
      filteredExpenses: [],
      startData: new Date()
    };
  },

  methods: {
    ...mapActions(['setActualExpenses']),
    getCategoryData() {
      const categories = {};
      let labels = [];
      const amounts = [];
      const colors = [];

      for (const expense of this.filteredExpenses) {
        const categoryName = expense.category_name;
        const amount = expense.amount;

        if (!categories[categoryName]) {
          categories[categoryName] = 0;
        }

        categories[categoryName] += amount;
      }

      for (const category in categories) {
        labels.push(category);
        amounts.push(categories[category]);
        colors.push(getRandomColor());
      }
      labels = labels.map(lab => `${lab} ${categories[lab]}`)

      return {
        labels,
        amounts,
        colors,
      };
    },
    filterExpenses() {
      if (Array.isArray(this.getExpenses)) {
        const currentDate = this.startData

        if (this.selectedPeriod === 'Miesiąc') {
          const currentMonth = currentDate.getMonth() + 1;
          const currentYear = currentDate.getFullYear();
          this.filteredExpenses = this.getExpenses.filter((expense) => {
            const expenseDate = new Date(expense.data);
            const expenseMonth = expenseDate.getMonth() + 1;
            const expenseYear = expenseDate.getFullYear();
            return expenseMonth === currentMonth && expenseYear === currentYear;
          });
        } else if (this.selectedPeriod === 'Tydzień') {
          const currentDay = currentDate.getDate();
          const currentWeekStart = currentDay - currentDate.getDay();
          const currentWeekEnd = currentWeekStart + 6;
          this.filteredExpenses = this.getExpenses.filter((expense) => {
            const expenseDate = new Date(expense.data);
            const expenseDay = expenseDate.getDate();
            return expenseDay >= currentWeekStart && expenseDay <= currentWeekEnd;
          });
        }
      } else {
        this.filteredExpenses = [];
      }
      this.setActualExpenses(this.filteredExpenses)
    },
    showPreviousPeriod() {
      if (this.selectedPeriod === 'Miesiąc') {
        const previousMonth = new Date(this.startData.getFullYear(), this.startData.getMonth() - 1, 1);
        this.startData = previousMonth;
      } else if (this.selectedPeriod === 'Tydzień') {
        const previousMonth = new Date(this.startData.getFullYear(), this.startData.getMonth(), this.startData.getDate() - 7);
        this.startData = previousMonth;
      }
      this.filterExpenses();
    },
    showNextPeriod() {
      if (this.selectedPeriod === 'Miesiąc') {
        const previousMonth = new Date(this.startData.getFullYear(), this.startData.getMonth() + 1, 1);
        this.startData = previousMonth;
      } else if (this.selectedPeriod === 'Tydzień') {
        const previousMonth = new Date(this.startData.getFullYear(), this.startData.getMonth(), this.startData.getDate() + 7);
        this.startData = previousMonth;
      }
      this.filterExpenses();
    },
  },
  watch: {
    getExpenses(newExpenses) {
      if (newExpenses.length > 0) {
        this.filterExpenses();
      }
    },
  },
};

function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
</script>

<style scoped>
.chart-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.doughnut-chart {
  max-height: 460px;
}

.chart-navigation {
  display: flex;
  justify-content: center;
  align-items: baseline;
}

.doughnut-div {
  position: relative;
}

.period-sum {
  position: absolute;
  top: 52%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-weight: bold;
  font-size: 3.5rem;
}

.date-div {
  margin-top: 35px;
  font-weight: bold;
  font-size: large;
}

</style>
