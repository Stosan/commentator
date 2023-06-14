package main

import (
	internal "commentator/internal/v1"
	"os"
	"os/signal"
	"time"
)

/*
|********************************
| Commentator application
*********************************
|
|
|
|
*/

func main() {
	e := internal.Start()
	// Wait for interrupt signal to gracefully shutdown the server with
	// a timeout of 5 seconds.
	quit := make(chan os.Signal)
	signal.Notify(quit, os.Interrupt)
	<-quit
	// healthCheck = "unhealthy"
	time.Sleep(1 * time.Second)
	internal.Stop(e)
}
