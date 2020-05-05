package middleware

// generated by glo

import (
	"github.com/gin-gonic/gin"
	"github.com/limoxi/ghost"
)

type AccountMiddleware struct{

}

func (this *AccountMiddleware) Init(){
	ghost.Info("AccountMiddleware loaded")
}

func (this *AccountMiddleware) PreRequest (ctx *gin.Context){

}

func (this *AccountMiddleware) AfterResponse(ctx *gin.Context){

}

func init(){
	ghost.RegisterMiddleware(&AccountMiddleware{})
}