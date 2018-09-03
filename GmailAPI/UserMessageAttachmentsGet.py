"""Retrieve an attachment from a Message.
"""

from oauth2client import file, client, tools
from apiclient import errors
from httplib2 import Http
from googleapiclient.discovery import build
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'


def GetAttachments(service, user_id, msg_id, store_dir):
  """Get and store attachment from Message with given id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: ID of Message containing attachment.
    store_dir: The directory used to store attachments.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    for part in message['payload']['parts']:
      if part['filename']:

        file_data = base64.urlsafe_b64decode(part['body']['data']
                                             .encode('UTF-8'))

        path = ''.join([store_dir, part['filename']])

        f = open(path, 'w')
        f.write(file_data)
        f.close()

  except errors.HttpError as err:
    print('An error occurred: %s' % err)


def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    GetAttachments(service, "me", "", "/attachs")

if __name__ == '__main__':
    main()