"""
Class that represents one job offer
"""


class JobOffer:

    def __init__(self, title: str, place: str,
                 salary: str, contract_type: str, contact_email: str,
                 description: str = "", salary_description: str = "") -> None:
        """
        Constructor
        :param title: job title
        :param place: place of work
        :param salary: offered salary
        :param contract_type: contract type
        :param contact_email: contact email
        :param description: additional information
        :rtype: None
        """
        self.title: str = title
        self.place: str = place
        self.salary: str = salary
        self.contract_type: str = contract_type
        self.contact_email: str = contact_email
        self.description: str = description
        self.salary_description: str = salary_description
