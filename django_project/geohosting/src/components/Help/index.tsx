import React, { CSSProperties, FC } from "react";

import {
  Box,
  Drawer,
  DrawerBody,
  DrawerCloseButton,
  DrawerContent,
  DrawerOverlay,
  Flex,
  IconButton,
  useDisclosure,
} from "@chakra-ui/react";
import { FaQuestionCircle, FaRegQuestionCircle } from "react-icons/fa";
import { DocsCrawlerPage } from "django-docs-crawler-react";

import "django-docs-crawler-react/dist/style.css";
import "./index.scss";

interface IHelp {
  isDrawer?: boolean;
  backgroundColor?: string;
  style?: CSSProperties | undefined;
}

const Help: FC<IHelp> = ({
  isDrawer,
  backgroundColor = "gray.500",
  style = {},
}) => {
  const {
    isOpen: isDrawerOpen,
    onOpen: onDrawerOpen,
    onClose: onDrawerClose,
  } = useDisclosure();
  const relativeUrl = (window.location.pathname + window.location.hash).replace(
    "/#",
    "",
  );

  const QuestionCircle = () => {
    if (isDrawerOpen) {
      return <FaQuestionCircle fontSize={"1.5rem"} />;
    } else {
      return <FaRegQuestionCircle fontSize={"1.5rem"} />;
    }
  };

  return (
    <>
      {isDrawer ? (
        <>
          <Flex
            p={4}
            color="white"
            _hover={{ bg: "blue.500", cursor: "pointer" }}
            w="full"
            onClick={onDrawerOpen}
            style={style}
          >
            <Box mr={3} fontSize="lg" display="flex" alignItems="center">
              <QuestionCircle />
            </Box>
            Help
          </Flex>
        </>
      ) : (
        <IconButton
          aria-label="Open menu"
          icon={<QuestionCircle />}
          onClick={onDrawerOpen}
          backgroundColor={backgroundColor}
          _hover={{ backgroundColor: backgroundColor, opacity: 0.8 }}
          minWidth={0}
        />
      )}
      <Drawer isOpen={isDrawerOpen} placement="right" onClose={onDrawerClose}>
        <DrawerOverlay />
        <DrawerContent minWidth={"600px"}>
          <DrawerCloseButton />
          <DrawerBody>
            <DocsCrawlerPage
              dataUrl={"/docs_crawler/data"}
              open={true}
              setOpen={onDrawerClose}
              relativeUrl={relativeUrl}
            />
          </DrawerBody>
        </DrawerContent>
      </Drawer>
    </>
  );
};

export default Help;
