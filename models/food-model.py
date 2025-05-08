from pydantic import BaseModel, Field

class regularFood(BaseModel):
    name : str = Field(min_length=1, max_length=50)
    description : str = Field(min_length=1, max_length=200)
    rating : int = Field(gt=-1, lt=6)
    price : float = Field(gt=0)
    spicy_level : int = Field(gt=-1, lt=6)
    is_vegan : bool = Field(default=False)
    is_gluten_free : bool = Field(default=False)

class dessert(BaseModel):
    name : str = Field(min_length=1, max_length=50)
    description : str = Field(min_length=1, max_length=200)
    rating : int = Field(gt=-1, lt=6)
    price : float = Field(gt=0)
    is_vegan : bool = Field(default=False)
    is_gluten_free : bool = Field(default=False)

class drink(BaseModel):
    name : str = Field(min_length=1, max_length=50)
    description : str = Field(min_length=1, max_length=200)
    rating : int = Field(gt=-1, lt=6)
    price : float = Field(gt=0)
    is_alcoholic : bool = Field(default=False)
    is_caffeine_free : bool = Field(default=False)

class combo(BaseModel):
    name : str = Field(min_length=1, max_length=50)
    description : str = Field(min_length=1, max_length=200)
    rating : int = Field(gt=-1, lt=6)
    price : float = Field(gt=0)
    is_vegan : bool = Field(default=False)
    is_gluten_free : bool = Field(default=False)
    is_alcoholic : bool = Field(default=False)