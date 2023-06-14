package postgres

import (
	"commentator/internal/config"
	"commentator/internal/v1/repo"
	"commentator/pkg/schemas"
	"fmt"
	"log"
	"time"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"
)

type DatabasebObject struct {
	Db *gorm.DB
	St repo.CommentatorRepoInterface
}

var DbObject DatabasebObject

// initialize database connection
func init() {
	var host, user, password, ssl string
	var db_err error
	_ = &config.ConfigApplication{}
	dbname := config.AppConfig.DBName
	port := config.AppConfig.DBPort
	host = config.AppConfig.DBHost
	user = config.AppConfig.DBUser
	password = config.AppConfig.DBPassword
	ssl = config.AppConfig.SSL

	// connection string
	psqlconn := fmt.Sprintf("host=%v user=%v password=%v dbname=%v port=%v sslmode=%v", host, user, password, dbname, port, ssl)
	// open database
	db, db_err := gorm.Open(postgres.Open(psqlconn), &gorm.Config{Logger: logger.Default.LogMode(logger.Silent)})
	if db_err != nil {
		log.Println(db_err)
	} else {
		log.Println("⚡️💾  Database ::Connected")
	}

	db_migration_err := db.AutoMigrate(
		&schemas.AppOperationsLog{},
		&schemas.CodeComment{})
	if db_migration_err != nil {
		log.Println("cannot migrate table", db_migration_err.Error())

	} else {
		log.Println("⚡️🚌  Database migration ::Done")
	}
	// check database
	sqlDB, sqldb_err := db.DB()
	if sqldb_err != nil {
		fmt.Println(sqldb_err)
	}
	// SetMaxIdleConns sets the maximum number of connections in the idle connection pool.
	sqlDB.SetMaxIdleConns(10)

	// SetMaxOpenConns sets the maximum number of open connections to the database.
	sqlDB.SetMaxOpenConns(100)

	// SetConnMaxLifetime sets the maximum amount of time a connection may be reused.
	sqlDB.SetConnMaxLifetime(time.Hour)
	//set Database object
	DbObject.Db = db
	DbObject.St = repo.NewCommentatorRepository(db)
}
