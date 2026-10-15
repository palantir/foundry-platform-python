# EmailMediaItemMetadata

Metadata for email media items.

## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**format** | EmailDecodeFormat | Yes |  |
**size_bytes** | int | Yes | Deprecated: use `sizeBytesLong`. Saturates at 2,147,483,647 for items of 2 GiB or larger.  |
**size_bytes_long** | MediaItemSizeBytes | Yes |  |
**sender** | List[Mailbox] | Yes | The sender(s) of the email. |
**date** | datetime | Yes | The date the email was sent. |
**attachment_count** | int | Yes | The number of attachments in the email. |
**to** | List[MailboxOrGroup] | Yes | The recipient(s) of the email. |
**cc** | List[MailboxOrGroup] | Yes | The CC recipient(s) of the email. |
**subject** | Optional[str] | No | The subject of the email. |
**attachments** | List[EmailAttachment] | Yes | The attachments of the email. |
**type** | Literal["email"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
