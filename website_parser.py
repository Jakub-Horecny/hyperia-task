"""
Parser for the website
"""

from bs4 import BeautifulSoup, Tag
import requests

from file_manager import FileManager
from job_offer import JobOffer


class Parser:
    WEB_SIDE_URL: str = "https://www.hyperia.sk"
    JOBS_URL: str = "/kariera/"

    JOBS_DIV_CLASS: str = "offset-lg-1 col-md-10"
    DESCRIPTION_DIV_CLASS: str = "hero-text col-lg-12"
    MAIN_INFO_DIV_CLASS: str = "col-md-4 icon"
    EMAIL_DIV_CLASS: str = "container position-contact"

    def __init__(self) -> None:
        """
        Constructor
        :rtype: None
        """
        self.file_manager: FileManager = FileManager()

    def get_all_jobs_from_website(self) -> None:
        """
        Gets all the jobs from hyperia web side and save them to a json file
        :rtype: None
        """
        html_text: bytes = requests.get(self.WEB_SIDE_URL + self.JOBS_URL).content
        soup: BeautifulSoup = BeautifulSoup(html_text, 'lxml')
        jobs: BeautifulSoup.ResultSet = soup.find_all('div', class_=self.JOBS_DIV_CLASS)

        # loops through all jobs
        jobs_list: list = []
        for job in jobs:
            (title, place, salary, contract_type, contact_email,
             description, salary_description) = self.__get_job_data(job)

            offer: JobOffer = JobOffer(title, place, salary, contract_type, contact_email,
                                       description, salary_description)
            jobs_list.append(offer)

        # saves to a file
        self.file_manager.save_as_json_file(jobs_list)

    def __get_job_data(self, job: Tag) -> [str, str, str, str, str, str]:
        """
        Gets data about one job offer
        :param job: one job offer
        :return: title, place, salary, contract type, contact email, description, salary description
        :rtype: [str, str, str, str, str, str]
        """
        address: Tag = job.find('a', href=True)
        job_text: bytes = requests.get(self.WEB_SIDE_URL + str(address['href'])).content
        soup: BeautifulSoup = BeautifulSoup(job_text, 'lxml')

        title: str = soup.find('h1').text
        description: str = soup.find('div', class_=self.DESCRIPTION_DIV_CLASS).find('p').text.strip()

        # loops through multiple informations in one div
        main_info: BeautifulSoup.ResultSet = soup.find_all('div', class_=self.MAIN_INFO_DIV_CLASS)
        main_info_list: list = []
        for info in main_info:
            data = info.find('p').find('br').next_siblings
            for dat in data:
                if dat.get_text() != '':
                    main_info_list.append(dat.get_text())

        email: str = soup.find('div', class_=self.EMAIL_DIV_CLASS).find('strong').text

        # if salary has no additional information
        if len(main_info_list) == 3:
            return title, main_info_list[0], main_info_list[1], main_info_list[2], email, description, ''
        return title, main_info_list[0], main_info_list[1], main_info_list[3], email, description, main_info_list[2]
