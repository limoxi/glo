package &_{resource_name}

import (
	"context"
	"github.com/limoxi/ghost"
)

type &_{resource_title}FillService struct {
	ghost.DomainService
}

func (this *&_{resource_title}FillService) Fill(&_{resource_name} *&_{resource_title}, fillOptions ghost.FillOptions){
    this.FillMany([]*&_{resource_title}{&_{resource_name}}, fillOptions)
}

func (this *&_{resource_title}FillService) FillMany(&_{resource_plural} []*&_{resource_title}, fillOptions ghost.FillOptions){
    if len(&_{resource_plural}) == 0{
        return
    }
}

func New&_{resource_title}FillService(ctx context.Context) *&_{resource_title}FillService{
	inst := new(&_{resource_title}FillService)
	inst.SetCtx(ctx)
	return inst
}