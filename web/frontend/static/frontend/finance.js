function daysInMonth(month, year) {
    return new Date(year, month, 0).getDate();
}

var app = new Vue({
    el: '#finance-app',
    delimiters: ['[[', ']]'],
    data: {
        serverData: [],
        chartData: [],
        each: 'day',
        label: [],
        targetDate: null
    },
    mounted: function(){
        this.fetchData(this.prepareChart);
    },
    methods: {
        prepareChart: function(){
            this.chartData = [];
            this.label = [];
            if (this.each == 'day') {
                if (this.targetDate == null)
                    date = new Date();
                else
                    date = new Date(this.targetDate);
                nbDays = daysInMonth(date.getMonth(), date.getFullYear());
                data = {
                    label : 'Income',
                    backgroundColor: 'rgb(255, 255, 100)',
                    yAxisID: 'y-axis-1',
                    data: []
                }
                for (var i = 1; i <= nbDays; i++){
                    this.label.push(i);
                    data.data.push(0);
                }
                this.serverData.forEach(function(d){
                    serverDataDate = new Date(d.time);
                    data.data[serverDataDate.getDate() - 1] = d.total_income;
                })
                this.chartData.push(data);
            }

            var ctx = document.getElementById('chart').getContext('2d');
            window.myBar = new Chart(ctx, {
				type: 'bar',
				data: {
                    labels: this.label,
                    datasets: this.chartData,
                },
				options: {
					responsive: true,
					title: {
						display: true,
						text: 'Data Keuangan HMIF'
					},
					tooltips: {
						mode: 'index',
						intersect: true
					},
					scales: {
						yAxes: [{
							type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
							display: true,
							position: 'left',
							id: 'y-axis-1',
						}],
					}
				}
			});
        },
        fetchData : function(callback){
            axios.get('api-finance/income-summary?each=day')
            .then((response) => {
                this.serverData = response.data;
                if (callback != null){
                    callback();
                }
            })
            .catch((err) => {
                console.log(err);
            })
        },
        getData : function(callback){
            axios.get('api-finance/income-summary?each=month')
            .then((response) => {
                this.serverData = response.data;
                this.prepareChart()
                window.myBar.update();
                if (callback != null){
                    callback();
                }
            })
            .catch((err) => {
                console.log(err);
            })
        }
    }
})