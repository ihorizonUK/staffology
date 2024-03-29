from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractAnalysisCategoryResponse")

@attr.s(auto_attribs=True)
class ContractAnalysisCategoryResponse:
    """
    Attributes:
        id (Union[Unset, str]): Analysis Category identifier
        name (Union[Unset, None, str]): Analysis Category Name
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET


    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        contract_analysis_category_response = cls(
            id=id,
            name=name,
        )

        return contract_analysis_category_response

