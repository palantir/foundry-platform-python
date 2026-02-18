# EmailMediaItemMetadata

Metadata for email media items.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | EmailDecodeFormat | Yes |  |
**size_bytes** | int | Yes | The size of the media item in bytes. |
**sender** | List[Mailbox] | Yes | The sender(s) of the email. |
**date** | datetime | Yes | The date the email was sent. |
**attachment_count** | int | Yes | The number of attachments in the email. |
**to** | List[MailboxOrGroup] | Yes | The recipient(s) of the email. |
**cc** | List[MailboxOrGroup] | Yes | The CC recipient(s) of the email. |
**subject** | Optional[str] | No | The subject of the email. |
**attachments** | List[EmailAttachment] | Yes | The attachments of the email. |
**type** | Literal["email"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
