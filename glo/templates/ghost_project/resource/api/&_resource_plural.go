package &_{resource_name}

import (
	"github.com/limoxi/ghost"
	bm_&_{resource_name} "&_{service_name}/business/model/&_{resource_name}"
)

type &_{resource_title_plural} struct {
	ghost.ApiTemplate

	GetParams struct {
        Filters ghost.Map `form:"filters"`
        WithOptions ghost.FillOptions `form:"with_option"`
        CurPage int `form:"cur_page"`
        PageSize int `form:"page_size"`
    }
}



func (this *&_{resource_title_plural}) Resource() string{
	return "&_{resource_name}.&_{resource_plural}"
}

func (this *&_{resource_title_plural}) Get() ghost.Response{
	ctx := this.GetCtx()
	params := this.GetParams
	&_{resource_name}Repo := bm_&_{resource_name}.New&_{resource_title}Repository(ctx)
	&_{resource_name}Repo.SetPage(params.CurPage, params.PageSize)
	&_{resource_plural} := &_{resource_name}Repo.GetByFilters(params.Filters)
	bm_&_{resource_name}.New&_{resource_title}FillService(ctx).FillMany(&_{resource_plural}, params.WithOptions)
	return ghost.NewJsonResponse(ghost.Map{
		"&_{resource_plural}": bm_&_{resource_name}.New&_{resource_title}EncodeService(ctx).EncodeMany(&_{resource_plural}),
		"page_info": &_{resource_name}Repo.GetPaginator().ToMap(),
	})
}

func init(){
	ghost.RegisterApi(&&_{resource_title_plural}{})
}
