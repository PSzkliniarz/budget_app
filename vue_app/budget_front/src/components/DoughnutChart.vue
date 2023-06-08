<template>
  <div class="chart-container">
    <h2>test</h2>
    {{ filteredExpenses }}
    <div class="filter-container">
      <v-select v-model="selectedPeriod" :items="periodOptions" label="Select Period" @change="filterExpenses "/>
      <button @click="showPreviousPeriod">Poprzedni okres</button>
      <button @click="showNextPeriod">Następny okres</button>
      {{ startData }}
    </div>
    <Doughnut v-if="filteredExpenses.length > 0" :data="chartData" :options="chartOptions"/>
    <h2 v-if="filteredExpenses.length === 0">Brak wydatków w tym okresie</h2>
    {{ periodSum }}
  </div>
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
            label: 'Amount',
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
      return ['Current Month', 'Current Week'];
    },
    periodSum() {
      return this.filteredExpenses.reduce((acc, obj) => acc + obj.amount, 0)
    }
  },
  data() {
    return {
      selectedPeriod: 'Current Month',
      filteredExpenses: [],
      startData: new Date()
    };
  },

  methods: {
    ...mapActions(['setActualExpenses']),
    getCategoryData() {
      const categories = {};
      const labels = [];
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

      return {
        labels,
        amounts,
        colors,
      };
    },
    filterExpenses() {
      if (Array.isArray(this.getExpenses)) {
        const currentDate = this.startData

        if (this.selectedPeriod === 'Current Month') {
          const currentMonth = currentDate.getMonth() + 1;
          const currentYear = currentDate.getFullYear();
          this.filteredExpenses = this.getExpenses.filter((expense) => {
            const expenseDate = new Date(expense.data);
            const expenseMonth = expenseDate.getMonth() + 1;
            const expenseYear = expenseDate.getFullYear();
            return expenseMonth === currentMonth && expenseYear === currentYear;
          });
        } else if (this.selectedPeriod === 'Current Week') {
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
      if (this.selectedPeriod === 'Current Month') {
        const previousMonth = new Date(this.startData.getFullYear(), this.startData.getMonth() - 1, 1);
        this.startData = previousMonth;
      } else if (this.selectedPeriod === 'Current Week') {
        const previousMonth = new Date(this.startData.getFullYear(), this.startData.getMonth(), this.startData.getDate() - 7);
        this.startData = previousMonth;
      }
      this.filterExpenses();
    },
    showNextPeriod() {
      if (this.selectedPeriod === 'Current Month') {
        const previousMonth = new Date(this.startData.getFullYear(), this.startData.getMonth() + 1, 1);
        this.startData = previousMonth;
      } else if (this.selectedPeriod === 'Current Week') {
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

<style>
.chart-container {
  width: 100%;
  height: 500px;
  display: flex;
  justify-content: center;
}
</style>
