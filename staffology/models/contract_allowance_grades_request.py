import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractAllowanceGradesRequest")

@attr.s(auto_attribs=True)
class ContractAllowanceGradesRequest:
    """
    Attributes:
        allowance_grade_payslip_text (Union[Unset, None, str]): Alternative text for display on the payslip (i.e. TLR1A)
        allowance_grade_annual_value (Union[Unset, float]): FTE value of allowance grade
        allowance_grade_effective_date (Union[Unset, datetime.date]): Effective date of the value
    """

    allowance_grade_payslip_text: Union[Unset, None, str] = UNSET
    allowance_grade_annual_value: Union[Unset, float] = UNSET
    allowance_grade_effective_date: Union[Unset, datetime.date] = UNSET


    def to_dict(self) -> Dict[str, Any]:
        allowance_grade_payslip_text = self.allowance_grade_payslip_text
        allowance_grade_annual_value = self.allowance_grade_annual_value
        allowance_grade_effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.allowance_grade_effective_date, Unset):
            allowance_grade_effective_date = self.allowance_grade_effective_date.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update({
        })
        if allowance_grade_payslip_text is not UNSET:
            field_dict["allowanceGradePayslipText"] = allowance_grade_payslip_text
        if allowance_grade_annual_value is not UNSET:
            field_dict["allowanceGradeAnnualValue"] = allowance_grade_annual_value
        if allowance_grade_effective_date is not UNSET:
            field_dict["allowanceGradeEffectiveDate"] = allowance_grade_effective_date

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowance_grade_payslip_text = d.pop("allowanceGradePayslipText", UNSET)

        allowance_grade_annual_value = d.pop("allowanceGradeAnnualValue", UNSET)

        _allowance_grade_effective_date = d.pop("allowanceGradeEffectiveDate", UNSET)
        allowance_grade_effective_date: Union[Unset, datetime.date]
        if isinstance(_allowance_grade_effective_date,  Unset):
            allowance_grade_effective_date = UNSET
        else:
            allowance_grade_effective_date = isoparse(_allowance_grade_effective_date).date()




        contract_allowance_grades_request = cls(
            allowance_grade_payslip_text=allowance_grade_payslip_text,
            allowance_grade_annual_value=allowance_grade_annual_value,
            allowance_grade_effective_date=allowance_grade_effective_date,
        )

        return contract_allowance_grades_request

