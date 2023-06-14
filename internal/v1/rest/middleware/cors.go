package middleware

import (
	"commentator/internal/config"
	"crypto/subtle"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

// This enables us interact with the Frontend Frameworks
func CORSMiddleware() echo.MiddlewareFunc {
	return middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins:     []string{"*"},
		AllowMethods:     []string{echo.GET, echo.HEAD, echo.PUT, echo.PATCH, echo.POST, echo.DELETE},
		AllowCredentials: true,
	})
}

func TrailMiddleware() echo.MiddlewareFunc {
	return middleware.RemoveTrailingSlash()
}

func BasicAuthMiddleware() echo.MiddlewareFunc {
	// // Use Basic Authentication middleware for all routes in the payment gateway group
	return middleware.BasicAuth(func(username, password string, c echo.Context) (bool, error) {
		// Compare the provided username and password with the ones defined in the config file
		if subtle.ConstantTimeCompare([]byte(username), []byte(config.AppConfig.AuthUsername)) == 1 &&
			subtle.ConstantTimeCompare([]byte(password), []byte(config.AppConfig.AuthPassword)) == 1 {
			// Return true if the username and password match
			return true, nil
		}
		// Return false if the username and password do not match
		return false, nil
	})
}
