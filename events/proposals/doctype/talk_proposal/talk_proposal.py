# Copyright (c) 2025, BWH Studios and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TalkProposal(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from events.events.doctype.proposal_speaker.proposal_speaker import ProposalSpeaker

		description: DF.TextEditor | None
		event: DF.Link
		speakers: DF.Table[ProposalSpeaker]
		status: DF.Literal["Review Pending", "Shortlisted", "Approved", "Rejected"]
		submitted_by: DF.Link
		title: DF.Data
	# end: auto-generated types

	pass
