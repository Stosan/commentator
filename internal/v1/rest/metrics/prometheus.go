package metrics

import (
	"time"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
)

//count the number of request made to the home endpoint
var APIHomeCounter = prometheus.NewCounter(
	prometheus.CounterOpts{
		Name: "api_home_request_count",
		Help: "No of api_home request handled by Api home endpoint",
	},
 )


 func OperationsMetrics() {
	go func() {
			for {
					opsProcessed.Inc()
					time.Sleep(2 * time.Second)
			}
	}()
}

var (
	opsProcessed = promauto.NewCounter(prometheus.CounterOpts{
			Name: "myapp_processed_ops_total",
			Help: "The total number of processed events",
	})
)