# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AS2ValidationSettings(Model):
    """The AS2 agreement validation settings.

    All required parameters must be populated in order to send to Azure.

    :param override_message_properties: Required. The value indicating whether
     to override incoming message properties with those in agreement.
    :type override_message_properties: bool
    :param encrypt_message: Required. The value indicating whether the message
     has to be encrypted.
    :type encrypt_message: bool
    :param sign_message: Required. The value indicating whether the message
     has to be signed.
    :type sign_message: bool
    :param compress_message: Required. The value indicating whether the
     message has to be compressed.
    :type compress_message: bool
    :param check_duplicate_message: Required. The value indicating whether to
     check for duplicate message.
    :type check_duplicate_message: bool
    :param interchange_duplicates_validity_days: Required. The number of days
     to look back for duplicate interchange.
    :type interchange_duplicates_validity_days: int
    :param check_certificate_revocation_list_on_send: Required. The value
     indicating whether to check for certificate revocation list on send.
    :type check_certificate_revocation_list_on_send: bool
    :param check_certificate_revocation_list_on_receive: Required. The value
     indicating whether to check for certificate revocation list on receive.
    :type check_certificate_revocation_list_on_receive: bool
    :param encryption_algorithm: Required. The encryption algorithm. Possible
     values include: 'NotSpecified', 'None', 'DES3', 'RC2', 'AES128', 'AES192',
     'AES256'
    :type encryption_algorithm: str or
     ~azure.mgmt.logic.models.EncryptionAlgorithm
    :param signing_algorithm: The signing algorithm. Possible values include:
     'NotSpecified', 'Default', 'SHA1', 'SHA2256', 'SHA2384', 'SHA2512'
    :type signing_algorithm: str or ~azure.mgmt.logic.models.SigningAlgorithm
    """

    _validation = {
        'override_message_properties': {'required': True},
        'encrypt_message': {'required': True},
        'sign_message': {'required': True},
        'compress_message': {'required': True},
        'check_duplicate_message': {'required': True},
        'interchange_duplicates_validity_days': {'required': True},
        'check_certificate_revocation_list_on_send': {'required': True},
        'check_certificate_revocation_list_on_receive': {'required': True},
        'encryption_algorithm': {'required': True},
    }

    _attribute_map = {
        'override_message_properties': {'key': 'overrideMessageProperties', 'type': 'bool'},
        'encrypt_message': {'key': 'encryptMessage', 'type': 'bool'},
        'sign_message': {'key': 'signMessage', 'type': 'bool'},
        'compress_message': {'key': 'compressMessage', 'type': 'bool'},
        'check_duplicate_message': {'key': 'checkDuplicateMessage', 'type': 'bool'},
        'interchange_duplicates_validity_days': {'key': 'interchangeDuplicatesValidityDays', 'type': 'int'},
        'check_certificate_revocation_list_on_send': {'key': 'checkCertificateRevocationListOnSend', 'type': 'bool'},
        'check_certificate_revocation_list_on_receive': {'key': 'checkCertificateRevocationListOnReceive', 'type': 'bool'},
        'encryption_algorithm': {'key': 'encryptionAlgorithm', 'type': 'str'},
        'signing_algorithm': {'key': 'signingAlgorithm', 'type': 'str'},
    }

    def __init__(self, *, override_message_properties: bool, encrypt_message: bool, sign_message: bool, compress_message: bool, check_duplicate_message: bool, interchange_duplicates_validity_days: int, check_certificate_revocation_list_on_send: bool, check_certificate_revocation_list_on_receive: bool, encryption_algorithm, signing_algorithm=None, **kwargs) -> None:
        super(AS2ValidationSettings, self).__init__(**kwargs)
        self.override_message_properties = override_message_properties
        self.encrypt_message = encrypt_message
        self.sign_message = sign_message
        self.compress_message = compress_message
        self.check_duplicate_message = check_duplicate_message
        self.interchange_duplicates_validity_days = interchange_duplicates_validity_days
        self.check_certificate_revocation_list_on_send = check_certificate_revocation_list_on_send
        self.check_certificate_revocation_list_on_receive = check_certificate_revocation_list_on_receive
        self.encryption_algorithm = encryption_algorithm
        self.signing_algorithm = signing_algorithm