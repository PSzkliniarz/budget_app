<template>
  <div class="chart-container">
    <Doughnut :data="chartData" :options="chartOptions"/>
  </div>
</template>

<script>
import {Doughnut} from 'vue-chartjs';
import {Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale} from 'chart.js';
import {mapGetters} from 'vuex';

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
  },

  methods: {
    getCategoryData() {
      const categories = {};
      const labels = [];
      const amounts = [];
      const colors = [];

      for (const expense of this.getExpenses) {
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
