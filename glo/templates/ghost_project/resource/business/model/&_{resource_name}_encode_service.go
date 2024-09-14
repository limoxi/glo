package &_{resource_name}

import (
	"context"
	"github.com/limoxi/ghost"
	ghost_utils "github.com/limoxi/ghost/utils"
)

type &_{resource_title}EncodeService struct {
	ghost.DomainService
}

func (this *&_{resource_title}EncodeService) Encode(&_{resource_name} *&_{resource_title}) *Encoded&_{resource_title}{
	return &Encoded&_{resource_title}{
		Id: &_{resource_name}.Id,
		CreatedAt: &_{resource_name}.CreatedAt.Format(ghost_utils.DEFAULT_TIME_LAYOUT),
	}
}

func (this *&_{resource_title}EncodeService) EncodeMany(&_{resource_plural} []*&_{resource_title}) []*Encoded&_{resource_title}{
	encoded&_{resource_title_plural} := make([]*Encoded&_{resource_title}, 0, len(&_{resource_plural}))
	for _, &_{resource_name} := range &_{resource_plural}{
		encoded&_{resource_title_plural} = append(encoded&_{resource_title_plural}, this.Encode(&_{resource_name}))
	}
	return encoded&_{resource_title_plural}
}

func New&_{resource_title}EncodeService(ctx context.Context) *&_{resource_title}EncodeService{
	inst := new(&_{resource_title}EncodeService)
	inst.SetCtx(ctx)
	return inst
}