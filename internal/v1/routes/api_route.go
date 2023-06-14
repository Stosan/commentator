package routes


import (
	"commentator/internal/config"
	"commentator/internal/database/postgres"
	"commentator/internal/v1/rest/metrics"
	sr"commentator/internal/v1/services"
	app_midd "commentator/internal/v1/rest/middleware"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func Router(e *echo.Group, cf config.ConfigApplication, dbO *postgres.DatabasebObject) {
	
	e.Use(app_midd.BasicAuthMiddleware())
	// Metrics
	prometheus.MustRegister(metrics.APIHomeCounter)
	e.Use(middleware.Recover())
	e.Use(middleware.RemoveTrailingSlash())
	//endpoints
	newcd := sr.NewCodeComment(dbO.St, dbO.Db,)
	e.GET("/metric", echo.WrapHandler(promhttp.Handler()))
	e.POST("/create-code-comments", newcd.MakeCodeComments)
}
