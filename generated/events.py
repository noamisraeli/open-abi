import pydantic


class Approval(pydantic.BaseModel):
	owner: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')
	spender: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')
	value: int


class Transfer(pydantic.BaseModel):
	from_: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')
	to: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')
	value: int
