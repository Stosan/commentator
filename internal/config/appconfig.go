package config

import (
	"log"
	"os"
	"github.com/joho/godotenv"
)

// Config stores the application configuration from environment variables
type ConfigApplication struct {
	Env     string 
	PORT     string 
	DBHost     string 
	DBPort     string 
	DBName     string 
	DBUser     string 
	DBPassword string
	SSL string
	AuthUsername string 
	AuthPassword string
	OPENAPI_KEY string
	
}
var AppConfig ConfigApplication
func init()  {
	paths := []string{".env", "../../.env", "../../../.env", "../../../../.env", "../../../../../.env"}
	var envErr error
	for _, path := range paths {
		envErr = godotenv.Load(path)
		if envErr == nil {
			break
		}
	}
	if envErr != nil {
		log.Fatal(envErr.Error())
	}

  AppConfig.Env     =os.Getenv("APPSETTING_GO_ENV")
  AppConfig.PORT     =os.Getenv("APPSETTING_PORT")
  AppConfig.DBHost     =os.Getenv("APPSETTING_DB_HOST")
  AppConfig.DBPort     =os.Getenv("APPSETTING_DB_PORT")
  AppConfig.DBName     =os.Getenv("APPSETTING_DB_DBNAME")
  AppConfig.DBUser     =os.Getenv("APPSETTING_DB_USER")
  AppConfig.DBPassword =os.Getenv("APPSETTING_DB_PASSWORD")
  AppConfig.SSL =os.Getenv("APPSETTING_DB_SSL")
  AppConfig.AuthUsername =os.Getenv("APPSETTING_AUTH_USERNAME")
  AppConfig.AuthPassword =os.Getenv("APPSETTING_AUTH_PASSWORD")
  AppConfig.OPENAPI_KEY = os.Getenv("APPSETTING_OPENAPI_KEY")

}
