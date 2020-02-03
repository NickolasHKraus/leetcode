class Solution(object):

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        to_send = []

        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.replace('.', '')
            local_name = local_name.split('+')[0]
            to_send.append('{}@{}'.format(local_name, domain_name))

        return len(set(to_send))
