source activate
export ENV=development

uvicorn src:api --reload
