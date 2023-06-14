package v1

import (
	"commentator/internal/config"
	"commentator/internal/database/postgres"
	"commentator/internal/v1/rest/middleware"
	"commentator/internal/v1/routes"
	"context"
	"log"
	"net/http"
	"net/http/pprof"
	"time"

	"github.com/labstack/echo/v4"
	e_mid "github.com/labstack/echo/v4/middleware"
)

func Start() *echo.Echo {
	e := echo.New()
	// Middleware
	//CORS
	e.Use(middleware.CORSMiddleware())
	e.Pre(middleware.TrailMiddleware())
	e.Use(e_mid.Logger())
	e.Use(e_mid.Recover())
	_ = &config.ConfigApplication{} //does nothing but vritical to loads config folder ahead with init
	databaseobject := &postgres.DbObject
	// Register the profiling routes
	// Create a separate ServeMux for profiling routes
	profilingMux := http.NewServeMux()
	profilingMux.HandleFunc("/debug/pprof/", pprof.Index)
	profilingMux.HandleFunc("/debug/pprof/cmdline", pprof.Cmdline)
	profilingMux.HandleFunc("/debug/pprof/profile", pprof.Profile)
	profilingMux.HandleFunc("/debug/pprof/symbol", pprof.Symbol)
	profilingMux.HandleFunc("/debug/pprof/trace", pprof.Trace)
	//servicegateway group route
	routergroup := e.Group("/api/v1")
	// Wrap the profiling ServeMux with Echo middleware
	e.Any("/debug/pprof/*", echo.WrapHandler(profilingMux))
	// Root route => handler
	e.GET("/", func(c echo.Context) error {
		var resp = map[string]interface{}{
			"ApplicationName":     "Commentator",
			"ApplicationOwner":    "Sam Ayo",
			"ApplicationVersion":  "1.0.0",
			"ApplicationEngineer": "Sam Ayo",
		}
		return c.JSON(http.StatusOK, resp)
	})
	//Run Server
	s := &http.Server{
		Addr:         ":" + string(config.AppConfig.PORT),
		ReadTimeout:  5 * time.Minute,
		WriteTimeout: 5 * time.Minute,
	}
	//s.SetKeepAlivesEnabled(false)
	e.HideBanner = true
	// Start server
	go func() {
		if err := e.StartServer(s); err != nil {
			log.Print(err.Error(), "shutting down the gateway server")
		}

	}()
	log.Println("⚡️🚀  Commentator by Sam ayo - Server ::Started")


	routes.Router(routergroup, config.AppConfig, databaseobject) //router
	return e
}

// Stop - stop the echo server
func Stop(e *echo.Echo) error {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	if err := e.Shutdown(ctx); err != nil {
		e.Logger.Fatal(err)
	}
	return nil
}
